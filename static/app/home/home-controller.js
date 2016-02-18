abdulBlog
  .controller('HomeController', ['$scope', '$http', function ($scope, $http) {

  	$scope.filters = [];
  	$http.get('/post/all').success(function(response){
  		$scope.posts = response;
  	});

  	$http.get('/tag/all').success(function(response){
  		$scope.tags = response;
  	});

  	$scope.$watch('filters', function(data){
  		console.log($scope.filters);
  	});

  	$scope.filterBy = function(tag){
  		$scope.filters.push(tag);
  		$scope.tags.splice(tag.id - 1, 1);
  	};

  	$scope.search = function(searchText){
  	};

  }]);
