blog.directive('loginModal', function(){
	return {
		templateUrl: '../static/app/auth/login.html',
		controller: ['$scope', '$location', 'AuthService',
			function ($scope, $location, AuthService) {
			  	$scope.login = function () {
			      // initial values
			      $scope.error = false;
			      $scope.disabled = true;
			      // call login from service
						// $auth.login(loginForm)
						// 	.then(function(response) {})
						// 	.catch(function(response) {});
			      AuthService.login($scope.loginForm.email, $scope.loginForm.password)

			        // handle success
			        .then(function () {
			          $location.path('/dashboard');
			          $scope.disabled = false;
			          $scope.loginForm = {};
			        })
			        // handle error
			        .catch(function () {
			          $scope.error = true;
			          $scope.errorMessage = "Invalid username and/or password";
			          $scope.disabled = false;
			          $scope.loginForm = {};
			        });

			    }
			}]
	}
});

blog.directive('hero', function(){
  return {
      templateUrl: '../static/app/directives/hero.html',
      restrict: 'E',
  }
});

blog.directive('notification', function(){
	var controller = ["$scope", "$timeout", function($scope, $timeout) {
		$scope.typeClass = "alert-" + $scope.type;
		$scope.$watch('show', function(oldVal, newVal, scope){
			$scope.showNotification = $scope.show || false;
			$timeout(function(){
				$scope.showNotification != $scope.showNotification;
			},2000);
		}, true);

	}];


	// var link = function(scope, elem, attr){
	// 	scope.$watch('show', function(oldVal, newVal, scope){
	// 		scope.showNotification = scope.show || false;
	// 		console.log(old, new);
	// 		$timeout(function(){
	// 			scope.showNotification != scope.showNotification;
	// 		},2000);
	// 	}, true);
	// };

	return {
		templateUrl: '../static/app/directives/notification.html',
		restrict: 'E',
		controller: controller,
		// link: link,
		scope : {
			type: '@',
			message: '@',
			show: '@'
		}
	}
});
