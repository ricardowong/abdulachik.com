var app = angular.module('dashboard', ['ngRoute', 'ngResource', 'ngSanitize', 'angularTrix', 'ngTagsInput']);

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
//
// app.directive('tagManager', function(){
//
//   var controller = function($scope){
//     $scope.search = function(title){
//       $scope.tagsList = [];
//       $scope.tags.map(function(tag){
//         if(tag.title === title){
//             $scope.tagsList.push(tag);
//         }
//         if($scope.tagsList.length > 0){
//           return $scope.tagsList;
//         } else {
//           console.log("not found");
//         }
//       })
//     };
//
//     $scope.addTag = function(tag){
//       $scope.tags.push({ title : tag , description : "unspecified"});
//     };
//
//     $scope.removeTag = function(tag){
//       console.log(tag)
//       $scope.tags.splice($scope.tags.indexOf(tag), 1);
//     }
//   };
//
//   return {
//     scope: {
//       tags: '='
//     },
//     restrict: 'E',
//     controller: controller,
//     templateUrl: '/static/js/app/directives/tagManager.html',
//     replace: true
//   }
// });
//
// app.directive('tag', function(){
//   var controller = function($scope) {
//     console.log("class");
//   };
//
//   return{
//     restrict: 'E',
//     controller: controller,
//     templateUrl: '/static/js/app/directives/tag.html',
//     replace: true,
//     scope: {
//       obj: '=',
//     }
//   }
// })
