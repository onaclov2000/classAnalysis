var computational_perception_robotics = [];
var computing_systems = [];
var high_performance_computing = [];
var interactive_intelligence = [];
var machine_learning = [];

computational_perception_robotics.push(['6505', '6520', '6550', '7520', '7530', '6140']);
computational_perception_robotics.push(['6601', '7641']);
computational_perception_robotics.push(['6475', '7495', '7499', '7636', '8803', '7630','7631', '7633', '7649', '88031']);

computing_systems.push(['6505']);
computing_systems.push(['6210', '6241', '6250', '6290', '6300', '6400']);
computing_systems.push(['6035', '6235', '6238', '6260', '6262', '6310', '6340', '6365', '6422', '6550', '6675', '7210', '7260', '7270', '7290', '7292', '7560', '8803FPL']);

high_performance_computing.push(['6140', '6220']);
high_performance_computing.push(['6140', '6220']);
high_performance_computing.push(['6221', '6230', '6241', '6290', '8803PNA', '6236', '8803PC']);

interactive_intelligence.push(['6300', '6505']);
interactive_intelligence.push(['6601', '7620', '7637', '7641']);
interactive_intelligence.push(['6440', '6460', '6465', '7634', '8803AGA', '7632', '7650', '8803CSS', '6795', '7610', '8803CC']);

machine_learning.push(['6505', '6520', '6550', '7510', '7520', '7530', '6140']);
machine_learning.push(['7641', '6740']);
machine_learning.push(['7540', '7545', '7616', '7646', '7650', '8803', '6240', '6242']);

var available = ['6210', '6250', '6300', '7641', '88031', '6290', '6310', '6440', '6505', '7637', '4495', '6475', '88032', '6035','6220', '6460', '7646', '88033'];
var foundational = ['6210', '6250', '6300', '7641', '6290', '6310', '6505', '7637', '4495', '88032', '6220'];

var set = {intersection : function(a,b){
            var result = [];
            for (i in a){
              var found = false;
              for (j in b){
                //console.log(a[i] + "===" + b[j]);
                if (a[i] === b[j])
                {
                  found = true;
                }
              }
              if (found){
                //console.log(a[i]);
                result.push(a[i]);
              }
            }
             return result;
            },
  union : function(a){
     return a[0].concat(a[1].concat(a[2]));
  
  }
};

console.log("Most Common Course");
// go through all combos :S
console.log('computational_perception_robotics and computing_systems');
console.log(set.intersection(computational_perception_robotics[0], computing_systems[0]));
console.log('computational_perception_robotics and high_performance_computing')
console.log(set.intersection(computational_perception_robotics[0], high_performance_computing[0]));
console.log('computational_perception_robotics and interactive_intelligence')
console.log(set.intersection(computational_perception_robotics[0], interactive_intelligence[0]));
console.log('computational_perception_robotics and machine_learning')
console.log(set.intersection(computational_perception_robotics[0], machine_learning[0]));
//
console.log('computing_systems and high_performance_computing')
console.log(set.intersection(computing_systems[0], high_performance_computing[0]));
console.log('computing_systems and interactive_intelligence')
console.log(set.intersection(computing_systems[0], interactive_intelligence[0]));
console.log('computing_systems and machine_learning')
console.log(set.intersection(computing_systems[0], machine_learning[0]));
//
console.log('high_performance_computing and interactive_intelligence')
console.log(set.intersection(high_performance_computing[0], interactive_intelligence[0]));
console.log('high_performance_computing and machine_learning')
console.log(set.intersection(high_performance_computing[0], machine_learning[0]));
//
console.log('interactive_intelligence and machine_learning');
console.log(set.intersection(machine_learning[0], interactive_intelligence[0]));


console.log(set.intersection(foundational, set.intersection(set.union(computational_perception_robotics), set.union(machine_learning))));

console.log(set.intersection(available, set.intersection(set.union(computational_perception_robotics), set.union(machine_learning))));


console.log("Machine Learning Courses Available");
console.log(set.intersection(available, set.union(machine_learning)));
console.log(set.intersection(foundational, set.union(machine_learning)));

console.log("Computational perception Available");
console.log(set.intersection(available, set.union(computational_perception_robotics)));
console.log(set.intersection(foundational, set.union(computational_perception_robotics)));

console.log("Interactive Intelligence Available");
console.log(set.intersection(available, set.union(interactive_intelligence)));
console.log(set.intersection(foundational, set.union(interactive_intelligence)));
