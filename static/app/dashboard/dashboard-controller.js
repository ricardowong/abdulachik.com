abdulBlog
	.controller('DashboardController', ['$scope', '$http', function($scope, $http){
		$scope.post = {};
		$scope.createPost = false;
		$scope.newPost = function(){
			$http.post('/post/new', $scope.post).success(function(response){
				$scope.createPost = !$scope.createPost;
			});
		};

	}]);	