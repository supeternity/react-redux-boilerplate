import { getCookie } from "./cookie";

export default function() {
  return getCookie('USER_TOKEN')
}
