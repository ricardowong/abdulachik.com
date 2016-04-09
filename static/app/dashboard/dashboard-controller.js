blog
	.controller('DashboardController', ['$scope', '$http', '$filter', function($scope, $http, $filter){
		$scope.postForm = { tags: [] };
		$scope.createPost = false;

		$http.get('/post/all').success(function(response){
			$scope.posts = response.length ? response : [];
		});

		$http.get('/tag/all').success(function(response){
			$scope.tags = response.length ? response: [];
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
				$scope.posts.push(response);
				if ($scope.postForm.tags){
					$http.post('/tagpost/' + response.id, { "tags" : $scope.postForm.tags }).success(function(response){
						$scope.postForm = { tags: [] };
					});
				}else{
					$scope.postForm = { tags: [] };
				}
			});
		};
		// TODO: finish updatePost tags problem
		$scope.updatePost = function(post){
			var url = '/post/' + post.slug;
			$http.put(url, post).success(function(response){
				if ($scope.postForm.tags.length > 0 && $scope.postForm.tags.length !== "undefined"){
					$http.post('/tagpost/' + response.id, { "tags" : $scope.postForm.tags }).success(function(response){
						$scope.postForm = { tags: [] };
					});
				}else{
					$scope.postForm = { tags: [] };
				}
			});
		};

		$scope.deletePost = function(post){
			var url = '/post/' + post.slug;
			var index = $scope.posts.indexOf(post);
			$scope.posts.splice(index, 1);
			$http.delete(url, post.slug);
		};

		$scope.addTag = function(tag){
			$http.post('/tag/new', { "title" : tag })
			.success(function(response){
				$scope.tagTitle = "";
				$scope.tags.push(response);
			});
		};

		$scope.tagPost = function(tag){
			tag.selected = true;
			$scope.postForm.tags.push(tag);
		};

		$scope.untagPost = function(tag, post){
			tag.selected = false;
			$http.delete('/tagpost/' + post.id + '/tag/' + tag.id + '/untag').success(function(response){
				var index = $scope.postForm.tags.indexOf(tag);
				$scope.postForm.tags.splice(index, 1);
			});
		};
		// TODO: should add a way to delete posts and tags together

	}]);
