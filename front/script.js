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
              },
              async deleteApp(id) {
                eel.del_file(id)()
                this.apps = JSON.parse(await eel.get_files_json()())
              },
              async renameApp(id) {
                result = prompt("Введите новое имя", "Новое имя");
                eel.change_name(id, result)()
                this.apps = JSON.parse(await eel.get_files_json()())
              },
              async openDirectory(id) {
                eel.open_containing_directory(id)()
              }
        },
        async created() {
            this.apps = JSON.parse(await eel.get_files_json()())
        }
      })