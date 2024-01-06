import { Component } from '@angular/core';
import FamilyTree from "@balkangraph/familytree.js";
import { HttpSerivceService } from '../http-serivce.service';
@Component({
  selector: 'app-tree',
  templateUrl: './tree.component.html',
  styleUrls: ['./tree.component.css']
})



export class TreeComponent {
  addMember() {
    let updateData: any = ""
    this.httpService.add_member(updateData).subscribe(() => {

    })
  }

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
            focusedNodeId = args.node.id;
            family.draw()
          });

          family.onUpdateNode((args) => {

            let updateData: any = args['updateNodesData'][0];
            let originalData;
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == updateData['id']) {

                originalData = users[i];
              }
            }
            delete updateData.gender;
            this.httpService.checkData(updateData).subscribe((res) => {
              let correctSpouseid: any = -1;
              let correctMotherid: any = -1;
              let correctFatherid: any = -1;
              let uid = res['uid'];
              if (res['Spouse'] != null) {

                let spouseData: any = res['Spouse'][0]
                correctSpouseid = parseInt(spouseData[0]['id']);
              }

              if (res['Mother'] != null) {

                let motherData: any = res['Mother'][0]
                correctMotherid = parseInt(motherData[0]['id']);
              }

              if (res['Father'] != null) {

                let fatherData: any = res['Father'][0]
                correctFatherid = parseInt(fatherData[0]['id']);
              }
              if (res == true) {


              } else {


                if (res['Spouse'] != null) {

                  let spouseData: any = res['Spouse'][0]
                  let promptText: string = "Please choose the correct Spouse for this user by typing the number associated with the user \n"
                  for (let i = 0; i < res['Spouse'][0].length; i++) {

                    promptText += `${spouseData[i]['id']}. Name: ${spouseData[i]['name']}, DOB: ${spouseData[i]['Birthday']}\n`
                  }
                  correctSpouseid = prompt(promptText);
                  correctSpouseid = parseInt(correctSpouseid);
                }

                if (res['Mother'] != null) {

                  let motherData: any = res['Mother'][0]

                  let promptText: string = "Please choose the correct Mother for this user by typing the number associated with the user \n"
                  for (let i = 0; i < res['Mother'][0].length; i++) {

                    promptText += `${motherData[i]['id']}. Name: ${motherData[i]['name']}, DOB: ${motherData[i]['Birthday']}\n`
                  }
                  correctMotherid = prompt(promptText);
                  correctMotherid = parseInt(correctMotherid);
                }

                if (res['Father'] != null) {

                  let fatherData: any = res['Father'][0]

                  let promptText: string = "Please choose the correct Father for this user by typing the number associated with the user \n"
                  for (let i = 0; i < res['Father'][0].length; i++) {

                    promptText += `${fatherData[i]['id']}. Name: ${fatherData[i]['name']}, DOB: ${fatherData[i]['Birthday']}\n`
                  }
                  correctFatherid = prompt(promptText);
                  correctFatherid = parseInt(correctFatherid);
                }
              }
              // Check if there has been any changes to the fields of Spouse, Mother and Father
              // If there has been changes, the data is commited to the database by a post request viua angular http
              if (correctSpouseid != -1) {
                let newData: any = { uid: uid, newId: correctSpouseid }
                this.httpService.updateSpouse(newData).subscribe((newData) => {

                })
              }
              if (correctMotherid != -1) {
                let newData: any = { uid: uid, newId: correctMotherid }

                this.httpService.updateMother(newData).subscribe((newData) => {

                })
              }

              if (correctFatherid != -1) {

                let newData: any = { uid: uid, newId: correctFatherid }
                this.httpService.updateFather(newData).subscribe((newData) => {

                })
              }
              // Send the values that could potentially have been changed but do not cause problems if they have been changend
              let updateRestData: any = { uid: updateData.id, name: updateData.name, age: updateData.age, Birthday: updateData.Birthday, DeathDate: updateData.DeathDate };
              this.httpService.updateRest(updateRestData).subscribe((updateRestData) => {


              })
            })



            function addMember(this: any) {

              this.httpService.add_member(updateData).subscribe(() => {

              })
            }

            family.draw();

          });


        }
      },
      (error) => { console.log(error); });
  }
}
