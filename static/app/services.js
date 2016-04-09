blog.factory('AuthService',
  ['$q', '$timeout', '$http', '$rootScope', '$cookies',
  function ($q, $timeout, $http, $rootScope, $cookies) {
    var cookie = $cookies;

    // create user variable
    $rootScope.user = null;
    function isLoggedIn() {
      if($rootScope.user) {
        return true;
      } else {
        return false;
      }
    }

    function login(email, password) {

      // create a new instance of deferred
      var deferred = $q.defer();

      // send a post request to the server
      $http.post('/login', {email: email, password: password})
        // handle success
        .success(function (data, status) {
          if(status === 200 && data.result){
            $rootScope.user = true;
            // cookie.put('session', data.sessionid);
            deferred.resolve();
          } else {
            $rootScope.user = false;
            deferred.reject();
          }
        })
        // handle error
        .error(function (data) {
          $rootScope.user = false;
          deferred.reject();
        });

      // return promise object
      return deferred.promise;

    }

    function logout() {

      // create a new instance of deferred
      var deferred = $q.defer();

      // send a get request to the server
      $http.get('/logout')
        // handle success
        .success(function (data) {
          $rootScope.user = false;
          // cookie.remove('session');
          deferred.resolve();
        })
        // handle error
        .error(function (data) {
          $rootScope.user = false;
          deferred.reject();
        });

      // return promise object
      return deferred.promise;

    }


    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout
      // ,register: register
    });
}])
.filter('cutText', [function(){
    return function(obj, limit){
        var keys = Object.keys(obj);
        if(keys.length < 1){
            return [];
        }

        var ret = new Object,
        count = 0;
        angular.forEach(keys, function(key, arrayIndex){
            if(count >= limit){
                return false;
            }
            ret[key] = obj[key];
            count++;
        });
        return ret.join();
    };
}]);
