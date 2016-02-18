abdulBlog
	.controller('DashboardController', ['$scope', '$http', function($scope, $http){
		$scope.postForm = {};
		$scope.createPost = false;
		$scope.posts = {};
		$http.get('/post/all').success(function(response){
			$scope.posts = response;
		});

		$scope.$watch('posts', function(data){
			$scope.posts = data;
		});

		$scope.newPost = function(publish){
			$scope.postForm.published = publish;
			$http.post('/post/new', $scope.postForm).success(function(response){
				$scope.createPost = !$scope.createPost;
				$scope.postForm = {};
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
	}]);	