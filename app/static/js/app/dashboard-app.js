var app = angular.module('dashboard', ['ngRoute', 'ngResource', 'ngSanitize', 'summernote', 'ngTagsInput']);

app.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/blog-landing', {
        templateUrl: '/static/js/app/dashboard/landing.html',
        controller: 'BlogIndexCtrl'
      })
      .when('/blog/new-post', {
        templateUrl: '/static/js/app/dashboard/new_post.html',
        controller: 'NewPostCtrl'
      })
      .when('/blog/timeline', {
        templateUrl: '/static/js/app/dashboard/timeline.html',
        controller: 'TimelineCtrl'
      })
      .when('/', {
        templateUrl: '/static/js/app/dashboard/index.html',
        controller: 'IndexCtrl'
      });
}]);

app.run(function($rootScope){
  $rootScope.dashboard = {
    title: 'Welcome to the dashboard',
    subtitle: 'manage all your content here'
  }
});

app.controller('IndexCtrl', function($scope, $rootScope){
  console.log("index");
});
