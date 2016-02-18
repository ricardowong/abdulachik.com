abdulBlog
  .controller('HomeController', ['$scope', '$http', function ($scope, $http) {
  	//example

  	$http.get('/post/all').success(function(response){
  		$scope.posts = response;
  	});

  }]);
