$(document).ready(function() {
    var defaultTextBox = function(textbox, default_val) {
        textbox = $(textbox);
        textbox.focus(function() {
            if($(this).val() == default_val) {
                $(this).val("");
                $(this).css('color', "#000000");
            }
        }).blur(function() {
            if($(this).val() != default_val && $(this).val() != "") {

            } else {
                $(this).val(default_val);
                $(this).css('color', '#cccccc');
            }
        });
    };


    //Add Recipe page
    if($("body").hasClass('recipes') && $("body").hasClass('add')) {
        $('#body form input[type=text]').each(function(i, el) {
            defaultTextBox(el, $(el).attr('value'));
        });

        $("a.add-another").click(function() {
            var num_ingredients = parseInt($("input#num_ingredients").val()) + 1;
            $("input#num_ingredients").val(num_ingredients);
            var html = '<p><label for="ingredient_' + num_ingredients + '">Ingredient ' + num_ingredients + '</label><br><input type="text" class="title" name="ingredient_' + num_ingredients + '" id="ingredient_' + num_ingredients + '" value="And another ingredient..." /><input type="text" style="margin-left:20px; width:170px;" class="title" name="ingredient_' + num_ingredients + '_quantity" id="ingredient_' + num_ingredients + '_quantity" value="Enter quantity..." /></p>';
            $(html).insertBefore(this);
            var ingredient_new = new LiveValidation('ingredient_' + num_ingredients);
            ingredient_new.add( Validate.Presence );
            defaultTextBox($('input#ingredient_' + num_ingredients), 'And another ingredient...');
            defaultTextBox($('input#ingredient_' + num_ingredients + '_quantity'), 'Enter quantity...');
        });
    }




});