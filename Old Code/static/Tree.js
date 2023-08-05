// fTree = []

// FamilyTree.templates.tommy.field_0 = FamilyTree.templates.tommy_male.field_0 = FamilyTree.templates.tommy_female.field_0 = '<text data-text-overflow="none" style="font-size: 18px;font-weight:bold;" fill="#ffffff" x="10" y="90" text-anchor="start">{val}</text>';

// var family = new FamilyTree(document.getElementById("tree"), {
//     mode: 'light',
//     mouseScrool: FamilyTree.none,
//     nodeBinding: {
//         field_0: "Name"
//     }
// });

// axios.get('/get_tree')
//     .then(function (response) {
//         for (let i = 0; i < response.data.length; i++) {

//             datar = response.data[i]
//             fTree.push(datar)
//         }

//     })

//     .catch(function (error) {

//         console.log(error);
//     })

// family.load(fTree)
// // function treeStuff() {
// //     axios.get('/get_tree')
// //         .then(function (response) {
// //             for (let i = 0; i < response.data.length; i++) {

// //                 datar = response.data[i]
// //                 console.log(datar)
// //                 if (datar[5] != null) {
// //                     if (datar[4] == false) {

// //                         if (datar[2] != null) {

// //                             fTree.push({ id: datar[6], mid: datar[5][0], fid: datar[5][1], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
// //                         } else {

// //                             fTree.push({ id: datar[6], mid: datar[5][0], fid: datar[5][1], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
// //                         }

// //                     } else {

// //                         if (datar[2] != null) {

// //                             fTree.push({ id: datar[7], mid: datar[5][0], fid: datar[5][1], pids: datar[6], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
// //                         } else {

// //                             fTree.push({ id: datar[7], mid: datar[5][0], fid: datar[5][1], pids: datar[6], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
// //                         }

// //                     }
// //                 } else {
// //                     if (datar[4] == false) {

// //                         if (datar[2] != null) {

// //                             fTree.push({ id: datar[6], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
// //                         } else {

// //                             fTree.push({ id: datar[6], Name: datar[0], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
// //                         }

// //                     } else {

// //                         if (datar[2] != null) {

// //                             fTree.push({ id: datar[7], Name: datar[0], pids: datar[6], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Died: new Date((datar[2]["_Date__year"], datar[2]["_Date__month"], datar[2]["_Date__day"])), Place: datar[3], Married: datar[4] });
// //                         } else {

// //                             fTree.push({ id: datar[7], Name: datar[0], pids: datar[6], Born: new Date(datar[1]["_Date__year"], datar[1]["_Date__month"], datar[1]["_Date__day"]), Place: datar[3], Married: datar[4] });
// //                         }

// //                     }
// //                 }
// //             }
// //             console.log(fTree);
// //             chart.load(fTree);
// //         })

// //         .catch(function (error) {

// //             console.log(error);
// //         })
// // }


// var jsonData = [
//     { "id": 1, "pid": 2, "gender": "male", "title": "Title", "name": "Father", "photo": "", "addr": "", "cn": "" },
//     { "id": 2, "pid": 1, "gender": "female", "title": "Title", "name": "Mother", "photo": "", "addr": "NY", "cn": "us" },
//     {
//         "id": 3, "pid": 4, "mid": 2, "fid": 1, "gender": "female", "title": "Title", "name": "Daughter",
//         "photo": "//unsplash.it/80/80", "addr": "USA", "cn": "us"
//     },
//     {
//         "id": 5, "mid": 2, "fid": 1, "gender": "male", "title": "Title", "name": "Jeff",
//         "photo": "", "addr": ""
//     },
//     { "id": 4, "pid": 3, "gender": "male", "title": "Title", "name": "Son-in-Law", "photo": "", "addr": "", "cn": "ca" },
// ];

// var params = {
//     data: jsonData, /*Local variable or file path*/
//     search: true, //false
//     container: "divFamily",
//     template: "circle" // "rounded" // "raised" // "tilted"
// };
// var tree = new Lineage(params);
// tree.load();
var jsonData = []
var params = {}
axios.get('/get_tree')
    .then(function (response) {
        for (let i = 0; i < response.data.length; i++) {

            datar = response.data[i]
            jsonData.push(datar)
        }
        console.log(jsonData)
        params = {
            data: jsonData, /*Local variable or file path*/
            search: true, //false
            container: "divFamily",
            template: "circle" // "rounded" // "raised" // "tilted"
        };
        var tree = new Lineage(params);
        tree.load();
    })

    .catch(function (error) {

        console.log(error);
    })

