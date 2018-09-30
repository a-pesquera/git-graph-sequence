window.master = window.gitgraph.branch("master");
window.gitgraph.commit("Initial commit");
window.develop = window.master.branch("develop");
window.develop.commit("Develop commit");
window.feature = window.develop.branch("feature/foo");
window.feature.commit({message: "First feature commit"});
window.feature.commit({message: "Final feature commit"});
window.feature.merge(window.develop);
window.develop.merge(window.master);
