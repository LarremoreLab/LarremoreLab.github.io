

// Define some parameters for display
var width = 1000,
height = 800,
baseCharge = -50,
distance = 35,
colorScale = 0.7,
radiusScale = 1.1,
radius = 7,
highlightMe = "",
scaleBy = "none",
/*
 colorListA = [
 //[150, 150, 150],
 [204,0,0],
 [204,102,0],
 [204,204,0],
 //[102,204,0],
 [0,204,0],
 //[0,204,102],
 [0,204,204],
 [0,102,204],
 [0,0,204]
 ];
 colorListC = [[208, 28, 139],
 [241, 182, 218],
 [184, 225, 134],
 [77, 172, 38]];
 */
colorListUPS = [[224,162,27], //orange
                [41,163,73], //green
                [27,89,224], //blue
                //[204,224,27]];
                [184,204,27],
                [50,50,100]
                ];
colorListSBM = [[31, 120, 180],
                [51, 160, 44],
                [227, 26, 28],
                [152, 78, 163],
                [255, 127, 0],
                [200, 200, 51]];
colorListCYS = [[217, 95, 2],
                [231, 41, 138],
                [230, 171, 2],
                [27, 158, 119],
                [117, 112, 179],
                [102, 166, 30]];
/*colorListCYS2= [[117, 112, 179],
 [117, 112, 179],
 [117, 112, 179],
 [230, 171, 2],
 [230, 171, 2],
 [230, 171, 2]];
 */
colorListCYS2= [[155, 30, 98],
                [155, 30, 98],
                [155, 30, 98],
                [102, 166, 30],
                [102, 166, 30],
                [102, 166, 30]];

var nodes = [],
links = [];
var linkType = "HVR1",
outlineby = "none",
colorby = "none",
HVRcolorby,
nComms = 0;
comms = [],
labels = [];
var force = d3.layout.force()
.links(links)
.nodes(nodes)
.charge(baseCharge)
.linkDistance(distance)
.size([width, height])
.on("tick",tick);
var svg = d3.select("#chart").append("svg")
.attr("width", width)
.attr("height", height);
var node = svg.selectAll(".node");
link = svg.selectAll(".link");
linkData = indexData[linkType];
//Push back all our nodes into nodes vector.
for (var i = 0; i<indexData.nodes.length; i++) {nodes.push(indexData.nodes[i]);}
//Push back all our links into links vector.
for (var i = 0; i<linkData.length; i++) {links.push(linkData[i]);}
draw();
function drawLegend() {
    svg.selectAll("#legend").remove();
    if (colorby=="ups")
    {
        comms = [0,1,2,3,4];
        labels = ["UPSA","UPSB","UPSC","UPSE","Not Determined"];
    }
    else if (HVRcolorby=="cystwocysfour")
    {
        comms = [0,3];
        labels = ["cys 2",
                  "cys 4"];
    }
    else if (colorby=="cyspolv")
    {
        comms = [0,1,2,3,4,5];
        labels = ["cys/polv 1",
                  "cys/polv 2",
                  "cys/polv 3",
                  "cys/polv 4",
                  "cys/polv 5",
                  "cys/polv 6"];
    }
    else if (colorby=="none")
    {
        comms = [];
        labels = [];
    }
    else if (colorby=="geneLength")
    {
        comms = [3792,5000,6000,7000,8000,9000,10000,11865];
        labels = ["3792 Nucleotides",5000,6000,7000,8000,9000,10000,11865];
        comms.forEach(function(d,i){
                      svg.append("circle")
                      .attr("id","legend")
                      .attr("r",function() {
                            if (scaleBy=="none")
                            {
                                return radius;
                            }
                            else
                            {
                                return radiusScaleFunction(comms[i]);
                            }
                            })
                      .attr("cx", 10)
                      .attr("cy", 2.3*radius*(i+1))
                      .style("fill", d3.hsl(rainbowFunction(comms[i],3792,11865),0.5,0.5))
                      .style("stroke", d3.rgb(255,255,255));
                      });
        labels.forEach(function(d,i){
                       svg.append("text")
                       .attr("id","legend")
                       .text(d)
                       .attr("x", 10+radius)
                       .attr("y", 2.3*radius*(i+1)+radius)
                       .attr("fill","black");
                       });
        return;
    }
    else
    {
        comms = [];
        labels = [];
        var rr;
        for (var pp=0; pp<nComms; pp++) {
            comms.push(pp);
            rr= pp+1;
            labels.push("inferred community " + rr);
        }
    }
    comms.forEach(function(d,i){
                  svg.append("circle")
                  .attr("id","legend")
                  .attr("r",radius)
                  .attr("cx", 10)
                  .attr("cy", 2.3*radius*(i+1))
                  .style("fill", computeColorInt(d))
                  });
    labels.forEach(function(d,i){
                   svg.append("text")
                   .attr("id","legend")
                   .text(d)
                   .attr("x", 10+radius)
                   .attr("y", 2.3*radius*(i+1)+radius)
                   .attr("fill","black");
                   });
}
function recomputeScale() {
    scaleBy = document.getElementById("scaleSelect").value;
    nodes.forEach(function(d) {
                  bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
                  .attr("r",computeRadius(d));
                  });
    changeHighlight();
    drawLegend();
}
function radiusScaleFunction(x)
{
    return (0.0001*x*radius);
}
function computeRadius(d) {
    if (scaleBy == "none")
    {
        return radius;
    }
    else
    {
        return (radiusScaleFunction(d.geneLength));
    }
}
function changeCharge() {
    var newCharge = document.getElementById("chargeSelect").value;
    force.charge(-newCharge);
    force.start();
}
function changeDistance() {
    var newDistance = document.getElementById("distanceSelect").value;
    force.distance(newDistance);
    force.start();
}
function recomputeData() {
    var menuItem = document.getElementById("dataSelect");
    linkType = menuItem.options[menuItem.selectedIndex].value;
	var shittyJS = links.length;
	for (var i = 0; i<shittyJS; i++) {links.pop();}
    draw();
	linkData = indexData[linkType];
	draw();
	for (var i = 0; i<linkData.length; i++) {links.push(linkData[i]);}
	draw();
}
function recomputeColor() {
    var menuItem = document.getElementById("colorSelect");
    HVRcolorby = menuItem.options[menuItem.selectedIndex].value;
    
    if (HVRcolorby[0]=="H")
    {
        var menuItem = document.getElementById("nCommsSelect");
        nComms = menuItem.options[menuItem.selectedIndex].value;
        colorby = HVRcolorby + " DCBM(" + nComms + ")";
        colorList = colorListSBM;
    }
    else {
        colorby = HVRcolorby;
        if (colorby=="cyspolv") {colorList = colorListCYS;}
        else if (colorby=="cystwocysfour") {
            colorList = colorListCYS2;
            colorby="cyspolv";
        }
        else {colorList = colorListUPS;}
    }
    svg.selectAll("circle.node")
    .style("fill",function(d){
           return computeColor(d);
           });
    drawLegend();
}
function rainbowFunction (x,min,max)
{
    return (210*(x-max)/(min-max));
}

function computeColor (d) {
    if (colorby=="none") {
        return d3.rgb(100,100,100);
    }
    else if (colorby=="geneLength"){
        return d3.hsl(rainbowFunction(d.geneLength,3792,11865),0.5,0.5);
    }
    else {
        return d3.rgb(colorList[d[colorby]][0],colorList[d[colorby]][1],colorList[d[colorby]][2]);
    }
}
function computeColorInt (i) {
    if (colorby=="none") {
        return d3.rgb(100,100,100);
    }
    else {
        return d3.rgb(colorList[i][0],colorList[i][1],colorList[i][2]);
    }
}
function highlightNode (d) {
    if (highlightMe.length == 0) {
        bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
        .style("stroke", d3.rgb(120,120,120))
        .attr("r",radiusScale*computeRadius(d));
    }
    else
    {
        if (d.name.indexOf(highlightMe) < 0) {
            bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
            .attr("r",radiusScale*computeRadius(d)/2)
            .style("stroke", d3.rgb(120,120,120));
        }
        else {
            bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
            .attr("r",radiusScale*radiusScale*computeRadius(d))
            .style("stroke", d3.rgb(0,0,0));
        }
    };
}
function highlightText(d) {
    textbit = svg.append("text").text("This is " + d.name.substring(0,d.name.indexOf("-")) + ".")
    .attr("x", 25)
    .attr("y", 2.3*radius*(comms.length+2))
    .attr("fill", "black")
    .attr("id","highlightText");
}
function changeHighlight() {
    highlightMe = document.getElementById("highlightSelect").value;
    highlightCounter = 0;
    if (highlightMe.length == 0) {
        nodes.forEach(function(d) {
                      d3.selectAll("#node_" + d.name.replace(/\./g,""))
                      .attr("r",computeRadius(d))
                      .style("stroke",d3.rgb(255,255,255));
                      });
    }
    else {
        nodes.forEach(function(d) {
                      if (d.name.indexOf(highlightMe) < 0) {
                      d3.selectAll("#node_" + d.name.replace(/\./g,""))
                      .attr("r",computeRadius(d)/2)
                      .style("stroke",d3.rgb(255,255,255));
                      }
                      else {
                      d3.selectAll("#node_" + d.name.replace(/\./g,""))
                      .style("stroke",d3.rgb(0,0,0))
                      .attr("r",radiusScale*computeRadius(d));
                      };})
    }
}
function unHighlightNode (d) {
    if (highlightMe.length == 0) {
        d3.selectAll("#node_" + d.name.replace(/\./g,""))
        .style("stroke", d3.rgb(255,255,255))
        .attr("r",computeRadius(d));
    }
    else
    {
        if (d.name.indexOf(highlightMe) < 0) {
            bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
            .attr("r",computeRadius(d)/2)
            .style("stroke", d3.rgb(255,255,255));
        }
        else {
            bert = d3.selectAll("#node_" + d.name.replace(/\./g,""))
            .attr("r",radiusScale*computeRadius(d))
            .style("stroke",d3.rgb(0,0,0));
        }
    }
    svg.selectAll("#highlightText").remove();
}
function tick() {
    node.attr("cx", function(d) { return d.x; })
    .attr("cy", function(d) { return d.y; })
    
    link.attr("x1", function(d) { return d.source.x; })
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; });
}
function draw() {
    
    link = link.data(force.links(), function(d) { return d.source.id + "-" + d.target.id; });
    link.enter().insert("line", ".node")
    .attr("class", "link")
    .style("stroke-width",1.0)
    .style("stroke",d3.rgb(150,150,150));
    link.exit().remove();
    
    node = node.data(force.nodes(), function(d) { return d.id;});
    node.enter().append("circle")
    .attr("class", "node")
    .attr("r",function(d) { computeRadius(d); })
    .attr("id",function(d) {
          return ("node_" + d.name.replace(/\./g,""));
          })
    .style("fill", function(d) {
           return computeColor(d);
           })
    .call(force.drag);
    node.exit().remove();
    
    node.on("mouseover",function(d) {
            highlightNode(d);
            highlightText(d);});
    node.on("mouseout",function(d) { unHighlightNode(d);});
    
    changeHighlight();
    force.start();
    for (var i=0; i<50; i++) {force.tick();}
}