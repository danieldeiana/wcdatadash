/*
    ***
        -- GRAPHS FOR TEAM STATS --
    ***
*/
queue()
    /*
        -- GETTING THE DATA --
    */
    .defer(d3.json, "/teamsdata")
    .await(makeTeamGraphs);

function makeTeamGraphs(error, teams){
    if (error) {
        console.log("Error receiving data-set with error: " + error.statusText);
        throw error;
    } else {
        console.log('teams object successfully received.');
        console.log(teams);
    }

    /*
        -- CREATING THE GRAPHS --
    */

    // -- DEFINING THE DIMENSIONS AND GROUPS --

    /*
        DATA FOR TEAMS
    name = db.Column(db.String(60), unique=True)
    wins = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    total_shots = db.Column(db.Integer)
    shots_on_target = db.Column(db.Integer)
    possesion = db.Column(db.Integer)
    total_passes = db.Column(db.Integer)
    yellows = db.Column(db.Integer)
    reds = db.Column(db.Integer)
    */

        // Render the charts
    //dc.renderAll();
}