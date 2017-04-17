//at some point, prevent enter pressing/make it call search function



var slow_write = _.debounce( function(term){
    var recipes = recipe_by_ing[term];
    if (recipes!=null){
        document.getElementById("recipe-list").innerHTML = "You searched for: " +term+"<br>"+recipes[0] + "<br>";
        for (i = 1; i < recipes.length; i++){
            document.getElementById("recipe-list").innerHTML += recipes[i] + "<br>";
        }
    }
    else{
        document.getElementById("recipe-list").innerHTML = 'This entry was not found.';
    }
}, 500);
