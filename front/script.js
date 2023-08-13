// Onclick of the button
document.querySelector("button").onclick = function () {
    // Call python's random_python function
    eel.random_python()(function(number){					
        // Update the div with a random number returned by python
        document.querySelector(".random_number").innerHTML = number;
    })
    }
    
    var sections = new Vue({
        el: '#sections',
        data: {


          sections: [
            { name: 'Игры' },
            { name: 'Работа' },
            { name: 'Сети' }
          ]
        }
      })
      
      var app_list = new Vue({
        el: '#app_list',
        data: {
          apps: [
            { name: 'Opera' },
            { name: 'League of Legend' },
            { name: 'Steam' },
            { name: 'VPN' }
          ]
        } ,
        methods: {
              openApp() {
                alert("👋 I am opened.")
              }
        },
        async mounted() {
                info = await eel.get_files_json()()
                alert(info)
        }
      })