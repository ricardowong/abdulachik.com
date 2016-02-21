abdulBlog
	.controller('BlogController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
		// pass
		$http.get('/post/' + $routeParams.postId)
			.success(function(response){
				$scope.post = response;
		});

		$http.get('/post/' + $routeParams.postId + '/tags')
			.success(function(response){
				console.log(response);
				$scope.tags = response;
			});
}]);