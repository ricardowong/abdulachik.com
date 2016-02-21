abdulBlog
	.controller('DashboardController', ['$scope', '$http', '$filter', function($scope, $http, $filter){
		$scope.postForm = {};
		$scope.createPost = false;
		$scope.posts = {};
		$scope.postForm.tags = [];
		$http.get('/post/all').success(function(response){
			$scope.posts = response;
		});

		$http.get('/tag/all').success(function(response){
			$scope.tags = response;
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
			} catch(e){console.log(e)}
		});
		$scope.newPost = function(publish){
			$scope.postForm.published = publish;
			$http.post('/post/new', $scope.postForm).success(function(response){
				$scope.createPost = !$scope.createPost;
				$scope.postForm = {};
				if ($scope.postForm.tags){
					$http.post('/tagpost/' + response.id, { "tags" : $scope.postForm.tags }).success(function(response){
						$scope.postForm.tags = [];
					});
				};
			});
		};

		$scope.updatePost = function(post){
			var url = '/post/' + post.id
			$http.put(url, post);
			$scope.postForm = {};
		};

		$scope.deletePost = function(post){
			var url = '/post/' + post.id;
			var index = $scope.posts.indexOf(post);
			$scope.posts.splice(index, 1);
			$http.delete(url, post.id);
		};

		$scope.addTag = function(tag){
			$http.post('/tag/new', { "title" : tag })
			.success(function(response){
				$scope.tagTitle = "";
				$scope.tags.push(response);
			});
		};

		$scope.tagPost = function(tag){
			$scope.postForm.tags.push(tag);
			$scope.containsTag(tag);
		};

		$scope.untagPost = function(tag){
			var index = $scope.postForm.tags.indexOf(tag);
			$scope.postForm.tags.splice(index, 1);
			$scope.containsTag(tag);
		};
	}]);	