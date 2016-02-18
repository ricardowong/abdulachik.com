abdulBlog
	.controller('BlogController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
		// pass
		$http.get('/post/' + $routeParams.postId)
			.success(function(data){
				$scope.post =  data;
		});
}]);