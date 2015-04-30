var app = angular.module('app', ['ngResource']);


app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.config(function($resourceProvider){
    $resourceProvider.defaults.stripTrailingSlashes = false;
});


app.factory("Label", function($resource){
    return $resource('/api/labels/:id/');
});

app.controller("LabelCtrl", function($scope, Label){
    $scope.new_label = new Label();
    Label.query(function(data){
	$scope.labels = data;
    });
    $scope.deleteLabel = function(id) {
	Label.delete({id: id}, function(data){
	    Label.query(function(data){
		$scope.labels = data;
	    });
	});
    };
    $scope.createLabel = function() {
	$scope.new_label.$save(function(response){
	    Label.query(function(data){
		$scope.labels = data;
		$scope.new_label = new Label();
	    });
	});
    };
});
