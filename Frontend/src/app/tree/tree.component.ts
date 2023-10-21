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
          let mid = base.mid;
          let fid = base.fid;
          if (mid == 0 && fid == 0) {

            let nameSpouse = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.pids) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, pids: base.pids, gender: "male", age: base.age, Birthday: base.birthday, DeathDate: base.deathDate, Spouse: nameSpouse })
          } else if (mid != 0 && fid == 0) {

            let nameMother = "";
            let nameSpouse = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.mid) {

                nameMother = users[i].name
              }
              if (users[i].id == base.pids) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, mid: mid, pids: base.pids, gender: "male", age: base.age, Birthday: base.birthday, DeathDate: base.deathDate, Mother: nameMother, Spouse: nameSpouse })
          } else if (mid == 0 && fid != 0) {

            let nameSpouse = "";

            let nameFather = "";
            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.fid) {

                nameFather = users[i].name
              }
              if (users[i].id == base.pids) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, fid: fid, pids: base.pids, gender: "male", age: base.age, Birthday: base.birthday, DeathDate: base.deathDate, Father: nameFather, Spouse: nameSpouse })

          } else if (mid != 0 && fid != 0) {

            let nameMother = "";
            let nameFather = "";
            let nameSpouse = "";

            for (let i = 0; i < users.length; i++) {

              if (users[i].id == base.mid) {

                nameMother = users[i].name
              }

              if (users[i].id == base.fid) {

                nameFather = users[i].name
              }
              if (users[i].id == base.pids) {

                nameSpouse = users[i].name
              }
            }
            newUsers.push({ id: base.id, name: base.name, mid: mid, fid: fid, pids: base.pids, gender: "male", age: base.age, Birthday: base.birthday, DeathDate: base.deathDate, Mother: nameMother, Father: nameFather, Spouse: nameSpouse })

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
            let newData: any;

            for (let i = 0; i < updateData.length; i++) {


            }
            console.log(originalData);
            console.log(updateData);
            family.draw();
          });

          // family.on("prerender", function (sender, args) {
          //   if (focusedNodeId == -1) {
          //     return;
          //   }
          //   var nodes = args.res.nodes;
          //   var node = nodes[focusedNodeId];
          //   node.tags.push('selected');
          //   iterate_parents(nodes, node);
          //   iterate_children(nodes, node);
          //   iterate_partners(nodes, node);
          //   focusedNodeId = -1;
          // });

          // function iterate_partners(nodes: any, node: any) {
          //   if (node.pids) {
          //     for (var i = 0; i < node.pids.length; i++) {
          //       var pnode = nodes[node.pids[i]];
          //       if (!pnode.tags.has('focused')) {
          //         pnode.tags.push('focused');
          //       }
          //     }
          //   }
          // }

          // function iterate_parents(nodes: any, node: any) {
          //   if (!node.tags.has('focused')) {
          //     node.tags.push('focused');
          //   }
          //   var mnode = nodes[node.mid];
          //   var fnode = nodes[node.fid];

          //   if (mnode) {
          //     iterate_parents(nodes, mnode);
          //   }

          //   if (fnode) {
          //     iterate_parents(nodes, fnode);
          //   }
          // }

          // function iterate_children(nodes: any, node: any) {
          //   if (node) {
          //     if (!node.tags.has('focused')) {
          //       node.tags.push('focused');
          //     }
          //     for (var i = 0; i < node.ftChildrenIds.length; i++) {
          //       var cnode = nodes[node.ftChildrenIds[i]];
          //       if (cnode.mid == node.id || cnode.fid == node.id) {
          //         iterate_children(nodes, cnode);
          //       }
          //     }
          //   }
          // }
        }
      },
      (error) => { console.log(error); });
  }
}
