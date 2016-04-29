blog
	.controller('DashboardController', ['$scope', '$http', '$filter', function($scope, $http, $filter){
		$scope.postForm = { tags: [] };
		$scope.createPost = false;

		$http.get('/post/all').success(function(response){
			$scope.posts = response.posts.length ? response.posts : [];
		});

		$http.get('/tag/all').success(function(response){
			$scope.tags = response.tags.length ? response.tags: [];
		});

		$scope.$watch('posts', function(data){
			$scope.posts = data;
		});

		$scope.$watch('postForm.tags', function(data){
			try{
				$scope.tags.map(function(tag){
					var selected;
					$scope.postForm.tags.map(function(pTag){
						tag.selected = tag.selected ? true : pTag.id == tag.id;
					});
					return tag;
				});
			} catch(e){
			}
		});
		
		$scope.newPost = function(publish){
			$scope.postForm.published = publish;
			
			$http.post('/post/new', $scope.postForm).success(function(response){
				$scope.createPost = !$scope.createPost;
				if (response.response == "OK!"){					
					$scope.posts.push($scope.postForm);
					$scope.postForm = { tags: [] };	
				}
			});
		};
		// TODO: finish updatePost tags problem
		$scope.updatePost = function(post){
			var url = '/post/' + post.id;
			$http.put(url, post).success(function(response){
				console.log(response);
			});
		};

		$scope.deletePost = function(post){
			var url = '/post/' + post.slug;
			var index = $scope.posts.indexOf(post);
			$scope.posts.splice(index, 1);
			$http.delete(url, post.slug);
		};

		$scope.addTag = function(tag){
			var tagObj = { "title" : tag }
			$http.post('/tag/new', tagObj)
			.success(function(response){
				$scope.tagTitle = "";
				$scope.tags.push(tagObj);
			});
		};

		$scope.tagPost = function(tag){
			tag.selected = true;
			$scope.postForm.tags.push(tag);
		};

		$scope.untagPost = function(tag){
			tag.selected = false;
			var index = $scope.postForm.tags.indexOf(tag);
			$scope.postForm.tags.splice(index, 1);
		};
	}]);
