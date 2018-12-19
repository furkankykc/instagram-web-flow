var table = document.getElementById("table");
if (table != null) {
    for (var i = 0; i < table.rows.length; i++) {
        for (var j = 0; j < table.rows[i].cells.length; j++)
            table.rows[i].cells[j].onclick = function () {
                tableText(this);
            };
    }
}

function tableText(tableCell) {
    alert(tableCell.innerHTML);
}

var buttonss = document.getElementById("followButton");
if (buttonss != null) {
    buttonss.onclick = function () {
        change(this)
    }
}

function change(e1) {
    if (e1.innerText == "Follow") {
        e1.className = "btn btn-following";
        e1.innerText = "Unfollow"

    } else {
        e1.className = "btn btn-not-following";

        e1.innerText = "Follow"
    }
}

$(function () {
    $(".identifyingClass").click(function () {
        var my_id_value = $(this).data('id');
        $(".modal-body .follow").innerText = " {% trans " + my_id_value + " as followers %";
        $("#myModalLabel").innerText = "32233";

    })
});
