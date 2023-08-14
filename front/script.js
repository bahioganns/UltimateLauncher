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
              openApp(id) {
                eel.open_file(id)()
              },
              async addApp() {
                eel.add_new_file()()
                this.apps = JSON.parse(await eel.get_files_json()())
              }
        },
        async created() {
            this.apps = JSON.parse(await eel.get_files_json()())
            alert(this.apps)
        }
      })