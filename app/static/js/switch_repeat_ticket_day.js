function switch_repeat_ticket() {
    var switch_repeat = document.getElementById('switch_repeat_ticket_day').checked

    // is true option habilited
    if (switch_repeat == true) {
        document.getElementById('repeat_ticket_day').style.display = 'block';
    }
    if (switch_repeat == false) {
        document.getElementById('repeat_ticket_day').value = 0;
        document.getElementById('repeat_ticket_day').style.display = 'none';
    }
}
switch_repeat_ticket()