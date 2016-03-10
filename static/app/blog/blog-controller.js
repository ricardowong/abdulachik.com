abdulBlog
	.controller('BlogController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
		// pass
		$http.get('/post/' + $routeParams.postSlug)
			.success(function(response){
				$scope.post = response;
				$http.get('/tagpost/' + response.id+ '/tags')
					.success(function(response){
						$scope.tags = response;
					});
		});

}]);