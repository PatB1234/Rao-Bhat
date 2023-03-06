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

