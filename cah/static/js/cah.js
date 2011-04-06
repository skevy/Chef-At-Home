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
            var first_ingredient = $('input#ingredient_1');
            defaultTextBox(first_ingredient, "Enter first ingredient...");
            
            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>