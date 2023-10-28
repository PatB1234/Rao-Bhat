import { Component } from '@angular/core';
import FamilyTree from "@balkangraph/familytree.js";
import { HttpSerivceService } from '../http-serivce.service';
@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.css']
})



export class TreeComponent {

  title = 'Rao Bhat';
  constructor(private httpService: HttpSerivceService) { }
  async ngOnInit() {


    let users: any;
    await this.httpService.getUsers().subscribe(
      (response) => {
        users = response
        let newUsers: any = []
        for (let i = 0; i < users.length; i++) {

          let base = users[i];
          let Mother = base.Mother;
          let Father = base.Father;
          if (Mother == 0 && Father == 0) {

            let nameSpouse = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.Spouse) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, pids: base.Spouse, gender: "male", age: base.age, Birthday: base.Birthday, DeathDate: base.DeathDate, Spouse: nameSpouse })
          } else if (Mother != 0 && Father == 0) {

            let nameMother = "";
            let nameSpouse = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.Mother) {

                nameMother = users[i].name
              }
              if (users[i].id == base.Spouse) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, mid: Mother, pids: base.Spouse, gender: "male", age: base.age, Birthday: base.Birthday, DeathDate: base.DeathDate, Mother: nameMother, Spouse: nameSpouse })
          } else if (Mother == 0 && Father != 0) {

            let nameSpouse = "";

            let nameFather = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.Father) {

                nameFather = users[i].name
              }
              if (users[i].id == base.Spouse) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, fid: Father, pids: base.Spouse, gender: "male", age: base.age, Birthday: base.Birthday, DeathDate: base.DeathDate, Father: nameFather, Spouse: nameSpouse })

          } else if (Mother != 0 && Father != 0) {

            let nameMother = "";
            let nameFather = "";
            let nameSpouse = "";

            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.Mother) {

                nameMother = users[i].name
              }

              if (users[i].id == base.Father) {

                nameFather = users[i].name
              }
              if (users[i].id == base.Spouse) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, mid: Mother, fid: Father, pids: base.Spouse, gender: "male", age: base.age, Birthday: base.Birthday, DeathDate: base.DeathDate, Mother: nameMother, Father: nameFather, Spouse: nameSpouse })

          }
        }
        const tree = document.getElementById('tree');
        if (tree) {
          var family = new FamilyTree(tree, {
            nodeBinding: {
              field_0: "name"
            },
          });
          family.load(newUsers);
          let focusedNodeId: any = 1;
          family.onNodeClick((args) => {
            console.log(args.node.id)
            focusedNodeId = args.node.id;
            family.draw()
          });

          family.onUpdateNode((args) => {

            //console.log(args);
            let updateData: any = args['updateNodesData'][0];
            let originalData;
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == updateData['id']) {

                originalData = users[i];
              }
            }
            delete updateData.gender;

            this.httpService.editUser(updateData).subscribe((updateData) => {

              console.warn(`WARNING DATA IS BEING POSTED!`)
            })
            console.log(originalData);
            console.log(updateData);
            family.draw();
          });


        }
      },
      (error) => { console.log(error); });
  }
}
