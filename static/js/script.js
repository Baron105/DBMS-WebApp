function changeReadMore(eventId) {
    
    const myButton = document.getElementById('read-more-btn-'+eventId);
    const threeDots = document.getElementById('three-dots-'+eventId);
    const fullDesc = document.getElementById('full-desc-'+eventId);
    const eventTiming = document.getElementById('event-timings-'+eventId);

    if (fullDesc.style.display === 'none' || fullDesc.style.display === '') {
        fullDesc.style.display = 'inline';
        threeDots.style.display = 'none';
        myButton.textContent = 'Read Less';
        eventTiming.style.display = 'none';
    } 
    
    else {
        fullDesc.style.display = 'none';
        threeDots.style.display = 'inline';
        myButton.textContent = 'Read More';
        eventTiming.style.display = 'flex';
    }
}

var et = document.querySelector('#my_variable').value

    function toggleDiv1() {
        var div = document.getElementById('profile-tab');
        var div2 = document.getElementById('organize-tab');
        var div3 = document.getElementById('edit-tab');
        var profile = document.getElementById('profile-content');
        var organize = document.getElementById('organize-content');
        var edit = document.getElementById('edit-content');
        div.style.backgroundColor = "#F2EFF3";
        div.style.color = "#4F708D"
        profile.style.display = "inherit";
        div2.style.backgroundColor = "inherit";
        div2.style.color = "inherit";
        organize.style.display = "none";
        div3.style.backgroundColor = "inherit";
        div3.style.color = "inherit";
        edit.style.display = "none";
    }
    function toggleDiv2() {
        var div = document.getElementById('profile-tab');
        var div2 = document.getElementById('organize-tab');
        var div3 = document.getElementById('edit-tab');
        var profile = document.getElementById('profile-content');
        var organize = document.getElementById('organize-content');
        var edit = document.getElementById('edit-content');
        div2.style.backgroundColor = "#F2EFF3";
        div2.style.color = "#4F708D";
        organize.style.display = "inherit";
        div.style.backgroundColor = "inherit";
        div.style.color = "inherit";
        profile.style.display = "none";
        div3.style.backgroundColor = "inherit";
        div3.style.color = "inherit";
        edit.style.display = "none";

    }
    function toggleDiv3() {
        var div = document.getElementById('profile-tab');
        var div2 = document.getElementById('organize-tab');
        var div3 = document.getElementById('edit-tab');
        var profile = document.getElementById('profile-content');
        var organize = document.getElementById('organize-content');
        var edit = document.getElementById('edit-content');
        div3.style.backgroundColor = "#F2EFF3";
        div3.style.color = "#4F708D";
        edit.style.display = "inherit";
        div.style.backgroundColor = "inherit";
        div.style.color = "inherit";
        profile.style.display = "none";
        div2.style.backgroundColor = "inherit";
        div2.style.color = "inherit";
        organize.style.display = "none";
    }
    function load(et){
        if(et == 1) {
            toggleDiv2();
        }
        else if(et == 2) {
            toggleDiv3();
        }
        else {
            toggleDiv1();
        }
    }