import createRouter from "router5";
import browserPlugin from "router5/plugins/browser";
import routes from "./routes";

export default function configureRouter() {
  const router = createRouter(routes, {
    defaultRoute: "main"
  }).usePlugin(
    browserPlugin({
      useHash: false
    })
  );
  return router;
}
