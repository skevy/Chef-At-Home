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

    if($("body").hasClass('has-table')) {
        $("a.favorite").click(function() {
            var $this = $(this);
            var item_id = parseInt($this.parents('tr').attr('data-id'));
            var item_type = $this.parents('table').attr('data-itemtype');
            $.ajax({
                type: 'POST',
                url: '/account/favorite/' + item_type + '/',
                data: { id: item_id },
                dataType: 'json',
                success: function(response) {
                    if(response.status == 'ok') {
                        if(response.action == 'favorited') {
                            $this.addClass('active');
                        } else if (response.action == 'unfavorited') {
                            $this.removeClass('active');
                        }
                    } else if(response.status == 'error') {

                    }
                }
            });
        });

        //get all favorited items (ids), then just loop through and add the class, pretty simple

        var url = "";
        if($('body').hasClass('recipes')) {
            url = "/recipes/favorites/";
        } else if($('body').hasClass('menus')) {
            url = "/menus/favorites/";
        } else if($('body').hasClass('meal-plans')) {
            url = "/meal-plans/favorites/";
        }

        if(url != "") {
            $.ajax({
                type: 'GET',
                url: url,
                dataType: 'json',
                success: function(response) {
                    $.each(response.items, function(i, item) {
                        $("tr[data-id=" + item + "] a.favorite").addClass('active');
                    });
                }
            });   
        }
    }



});