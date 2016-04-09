blog
  .controller('HomeController', ['$scope', '$http', function ($scope, $http) {

  	$scope.filters = [];

  	$http.get('/post/all').success(function(response){
  		$scope.posts = response.length ? response : [];

  	});

  	$http.get('/tag/all').success(function(response){
  		$scope.tags = response.length ? response : [];
  	});

  	$scope.filterBy = function(tag){
  		var index = $scope.tags.indexOf(tag);
  		$scope.filters.push(tag);
  		$scope.tags.splice(index, 1);
  	};

  	$scope.removeFilter = function(tag){
  		var index = $scope.filters.indexOf(tag);
  		$scope.filters.splice(index, 1);
  		$scope.tags.push(tag);
  	}

  	$scope.search = function(searchText){
  		$scope.searchTerm = searchText;
  	};

  	$scope.$watch('tagSearch', function(data){
  		try{
  			if (data.length == 0 || !data){
  				$scope.searchTerm = "";
  			}
  		} catch (e){
  		}
  	});

  }]);
