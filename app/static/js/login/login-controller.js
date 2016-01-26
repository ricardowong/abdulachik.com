abdulBlog
  .controller('LoginController', ['$scope', '$firebaseSimpleLogin', '$location', 
  	function ($scope, $firebaseSimpleLogin, $location) {
  	var firebaseObj = new Firebase("https://blinding-inferno-2180.firebaseio.com");
  	var loginObj = $firebaseSimpleLogin(firebaseObj);

  	$scope.SignIn = function(){
  		console.log($scope);
  		var username = $scope.user.email;
  		var password = $scope.user.password;
  		loginObj.$login('password', {
            email: username,
            password: password
        })
        .then(function(user) {
        	$location.path('/dashboard').replace();
            console.log('Authentication successful', user);
        }, function(error) {
            console.log('Authentication failure', error);
        });
  	}

  }]);
