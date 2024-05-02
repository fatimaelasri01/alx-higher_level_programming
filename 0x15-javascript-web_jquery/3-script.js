// uses the jQuery API to add a red class to the header
// when the user clicks on the tag DIV#red_header

$('div#red_header').click(function () {
    $('header').addClass('red');
});
