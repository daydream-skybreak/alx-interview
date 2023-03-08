#!/usr/bin/node
const request = require('request')
const rootApi = 'https://swapi-api.alx-tools.com/api/films/'
if (process.argv.length > 2) {
    request(`${rootApi}${process.argv[2]}`, (err, _, body) => {
        if (err) console.log("There is a problem with the api")

        const charactersApi = JSON.parse(body).characters;
        const charPromise = charactersApi.map(
            api => new Promise(
                (resolve, reject) => {
                    request(api,
                        (apiErr, __, apiBody) => {
                            if (apiErr) {
                                reject("couldn't resolve api")
                            }
                            resolve(JSON.parse(apiBody).name)
                        })
                }
            )
        )
        Promise.all(charPromise)
            .then(names => console.log(names.join('\n')))
            .catch(err => console.error(err))
    })
}