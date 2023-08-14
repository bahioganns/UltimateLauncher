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
          apps: []
        } ,
        methods: {
              openApp(number) {
                alert("i am opened " + number)
                //eel.execute_app()()
              },
              async addApp() {
                this.apps.push({name: "inserter"})
              }
        },
        async created() {
            this.apps = JSON.parse(await eel.get_files_json()())
            alert(this.apps)
        }
      })