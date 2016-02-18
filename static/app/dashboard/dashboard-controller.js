abdulBlog
	.controller('DashboardController', ['$scope', '$http', '$filter', function($scope, $http, $filter){
		$scope.postForm = {};
		$scope.createPost = false;
		$scope.posts = {};
		$scope.tagsPost = [];
		$http.get('/post/all').success(function(response){
			$scope.posts = response;
		});

		$scope.$watch('createPost', function(value){ console.log(value)});
		$http.get('/tag/all').success(function(response){
			$scope.tags = response;
		});

		$scope.$watch('posts', function(data){
			$scope.posts = data;
		});

		$scope.newPost = function(publish){
			$scope.postForm.published = publish;
			$http.post('/post/new', $scope.postForm).success(function(response){
				$scope.createPost = !$scope.createPost;
				$scope.postForm = {};
				if ($scope.tagsPost){
					$http.post('/tagpost/' + response.id, { "tags" : $scope.tagsPost }).success(function(response){
						$scope.tagsPost = [];
					});
				};
			});
		};

		$scope.updatePost = function(post){
			var url = '/post/' + post.id
			$http.put(url, post);
		};

		$scope.deletePost = function(post){
			var url = '/post/' + post.id
			$scope.posts.splice(post.id - 1, 1);
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
			$scope.tagsPost.push(tag);
		};

		$scope.untagPost = function(tag){
			var index = $scope.tagsPost.indexOf(tag);
			$scope.tagsPost.splice(index, 1);
		};

	}]);	