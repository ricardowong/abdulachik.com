blog
	.controller('BlogController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
		$http.get('/post/' + $routeParams.postid)
			.success(function(response){
				$scope.post = response;
		});
}]);
