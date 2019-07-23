// subroutes future

function route(url, view, subroutes) {
  return {
    path: url,
    component: import(`../pages/${view}.jsx`)
  }
}

const routes = [
  route('/', 'Main'),
  route('/manage/:slug', 'Manage'),
  route('/project/:slug', 'Project')
];

export default routes;