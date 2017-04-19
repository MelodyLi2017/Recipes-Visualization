//things to check: special equipment "ingredients" and "to blah blah blah" recipes
//takes in recipe name
//do the per serving thing (most of the recipes have calories), filter out recipes that don't have a calorie count
//figure out why some recipes don't work
//get information for nicole
function create_graph (recipe, recipe_ing, ing_nut, scales, x, y){
    //nutrition strings as in data files
    console.log(recipe_ing);
    //var nutrition_array = ['Energ_Kcal', 'Lipid_Tot', 'Cholestrl', 'Carbohydrt',
    //'Fiber_TD', 'Sugar_Tot', 'Protein', 'Calcium', 'Iron', 'Vit_A', 'Vit_C'];
    var nutrition_array = ['Energ_Kcal', 'Lipid_Tot', 'Carbohydrt', 'Protein',];
    //{ing1:{NDBNo:#, magnitude:#, unit: 'gram'}, ing2: {NDBNo:#, magnitude:#, unit: 'gram'}}
    var ing_full = recipe_ing[recipe];
    var calories = recipe_cal[recipe];
    //at some point in time, filter out recipes with > 11 ingredients
    var ing_list = Object.keys(ing_full);
    for (var i = 0; i < nutrition_array.length; i++){
        var agg_x = 15;
        var agg_nutrients = 0;
        var ratio = 0;
        for (var j = 0; j < ing_list.length; j++){
            var ing = ing_list[j];
            var NDBNo = ing_full[ing]['NDBNo'];
            // if (i == 0){
            //     console.log(ing);
            // }
            if (ing_nut[NDBNo]!=null){
                var amount_per = Number(ing_nut[NDBNo][nutrition_array[i]]);
                //console.log(calories);
                //console.log("amount of " + nutrient_list[i]+" per 100 gram: " + amount_per);
                if (ing_full[ing]['unit']!='gram'){
                    var amount_recipe = ing_full[ing]['magnitude'];
                }
                else{
                     var amount_recipe = Number(ing_full[ing]['magnitude'])/100;
                }
                var amount_recipe = Number(ing_full[ing]['magnitude'])/100;
                if (i == 0){
                    var tot_nutrients = Number(calories)/ing_list.length;
                }
                else{
                    var tot_nutrients = amount_recipe*amount_per//*ratio;
                }
                // console.log(ing);
                // console.log(tot_nutrients);
                // console.log(nutrition_array[i]);
                d3.select("#bars")
                .append("rect")
                .attr("class",ing)
                .attr("x", agg_x + 100)
                .attr("y", y+ i*60)
                .attr("height", 30)
                .attr("width", scales[i](tot_nutrients))
                .attr("fill", color_scale[j])
                .attr("stroke", color_scale[j]);
                //we're going to have problems with recipes with more than 11 ingredients
                agg_x += scales[i](Number(amount_recipe)*Number(amount_per));
                agg_nutrients+=amount_recipe*amount_per;
            }
        }
        if (i == 0){
            if (calories > agg_nutrients){
                console.log("something is wrong: " + agg_nutrients);
            }
            else{
                ratio = calories/agg_nutrients;
            }
        }
    }
}

function create_axis (scales, x, y, domain){
    //[                       Calories,      Fat,       Cholesterol,     crbs, 
    /*var nutrient_domains = [[0, 2000*1.2], [0, 65*1.2], [0, 300*1.2], [0, 300*1.2],
    //Fiber,       Sugar,       Protein         calc,         iron, 
    [0, 25*1.3], [0, 50*1.3], [0, 50*1.3], [0, 1000*1.3], [0, 18*1.3],
    //vit a, vitc]
    [0, 5000*1.3], [0, 60*1.3]];
    var axes = [];
    for (var k = 0; k < nutrient_domains.length; k++){
        scale = d3.scaleLinear().domain(nutrient_domains[k]).range([0, 500]);
        scales.push(scale);
        var axis = d3.axisTop(scale);
        var y_coord = k*100 + 50;

        d3.select("#text")
        .append("text")
        .text(nutrient_list[k])
        .attr("x", 13)
        .attr("y", y_coord-30);
    [0, 5000*1.2], [0, 60*1.2]];*/
	var nutrient_domains = [[0, domain[0]], [0, domain[1]], [0, domain[2]], [0, domain[3]]];
    var axes = [];

    for (i = 0; i < nutrient_domains.length; i++){
        scale = d3.scaleLinear().domain(nutrient_domains[i]).range([0, 550]);
        scales.push(scale);
        var axis = d3.axisTop(scale);
        var y_coord = i*60 + y;

        d3.select("#text")
        .append("text")
        .text(nutrient_list[i])
        .attr("x", x)
        .attr("y", y_coord + 15);

        d3.select("#axes")
        .append("g")
        .style("font-size", 11)
        .attr("transform", "translate(115, " + y_coord + ")" )
        .call(axis);
    }
}

function findMax(recipe, recipe_ing, ing_nut, recommend){
    //nutrition strings as in data files
	max = [];
    //nutrition strings as in data files
    console.log(recipe_ing);
    //var nutrition_array = ['Energ_Kcal', 'Lipid_Tot', 'Cholestrl', 'Carbohydrt',
    //'Fiber_TD', 'Sugar_Tot', 'Protein', 'Calcium', 'Iron', 'Vit_A', 'Vit_C'];
    var nutrition_array = ['Energ_Kcal', 'Lipid_Tot', 'Carbohydrt', 'Protein',];
    //{ing1:{NDBNo:#, magnitude:#, unit: 'gram'}, ing2: {NDBNo:#, magnitude:#, unit: 'gram'}}
    var ing_full = recipe_ing[recipe];
    //console.log(ing_full);
    //at some point in time, filter out recipes with > 11 ingredients
    var ing_list = Object.keys(ing_full);
    for (var i = 0; i < nutrition_array.length; i++){
        var agg_x = 0;
        for (var j = 0; j < ing_list.length; j++){
            var ing = ing_list[j];
            var NDBNo = ing_full[ing]['NDBNo'];
            // if (i == 0){
            //     console.log(ing);
            // }
            if (ing_nut[NDBNo]!=null){
                var amount_per = Number(ing_nut[NDBNo][nutrition_array[i]]);
                //console.log(ing_nut[NDBNo]['Shrt_Desc']);
                //console.log("amount of " + nutrient_list[i]+" per 100 gram: " + amount_per);
                if (ing_full[ing]['unit']!='gram'){
                    var amount_recipe = ing_full[ing]['magnitude'];
                }
                else{
                     var amount_recipe = Number(ing_full[ing]['magnitude'])/100;
                }
                var amount_recipe = Number(ing_full[ing]['magnitude'])/100;
                agg_x += (Number(amount_recipe)*Number(amount_per));
            }
        }
		if (agg_x > recommend[i])
			max.push(agg_x);
		else
			max.push(recommend[i])
    }
	return max;
}