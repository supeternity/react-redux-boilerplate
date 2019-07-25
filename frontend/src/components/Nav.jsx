import React from "react";
import { connect } from "react-redux";
import { BaseLink } from "react-router5";

function Nav(props) {
  const { router } = props;
  return (
    <nav>
      <BaseLink router={router} routeName="main">
        Boilerplate main page
      </BaseLink>
      <BaseLink router={router} routeName="links">
        Список ссылок
      </BaseLink>
      <BaseLink router={router} routeName="links.create">
        Создать ссылку
      </BaseLink>
      <BaseLink router={router} routeName="upload" routeParams={{ id: 1 }}>
        Загрузка проекта
      </BaseLink>
      <BaseLink router={router} routeName="project" routeParams={{ id: 1 }}>
        Просмотр проекта
      </BaseLink>
    </nav>
  );
}

export default connect(state => state.router.route)(Nav)
