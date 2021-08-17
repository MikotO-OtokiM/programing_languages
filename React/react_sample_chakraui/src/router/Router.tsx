import { memo, VFC } from "react";
import { Route, Switch } from "react-router-dom";

import { Login } from "../components/pages/Login";
import { Page404 } from "../components/pages/Page404";
import { HeaderLayout } from "../components/templates/HeaderLayout";
import { LoginUserProvider } from "../providers/LoginUserProvider";
import { homeRoutes } from "./HomeRouters";

export const Router: VFC = memo(() => {
  return (
    /**
     * react-router-dom で画面遷移させる場合は、Switch タグ内に
     * path 属性にてパスを指定した Route タグ（遷移画面）を指定する
     * 遷移画面の指定方法は以下の 2 つ
     * ・Route タグで遷移先画面のコンポーネントを囲う
     * ・Route タグ内の render 属性にて、アロー関数で遷移先画面のコンポーネントを
     * 　指定する
     */
    <Switch>
      {/* 
      Context を利用してグローバルに値を利用する場合は、作成した Provider タグで
      囲った範囲で利用できる
      */}
      <LoginUserProvider>
        {/*
        ログイン画面を指定
        ルート画面となるため、exact を指定し、パスの完全一致で
        遷移するようにする
        */}
        <Route exact path="/">
          <Login />
        </Route>
        {/*
        ログイン後の画面を /home で設定
        render 属性のアロー関数の中の Switch タグ内で
        ログイン後の遷移画面を指定する
        render 関数の props にある match の中の url に /home が入っている
        これを利用することで、/home 配下で確実に遷移させることができる
        render={(props) => ()}
        console.log(props)
        */}
        <Route
          path="/home"
          render={({ match: { url } }) => (
            <Switch>
              {/* HomeRouters.tsx で設定した画面を map で回す */}
              {homeRoutes.map((route) => (
                // map で処理する場合は、key の指定が必要
                // path は /home に続けて各ページのパスを連結
                <Route
                  key={route.path}
                  exact={route.exact}
                  path={`${url}${route.path}`}
                >
                  {/* ヘッダー有りのレイアウトでページを表示 */}
                  <HeaderLayout>{route.children}</HeaderLayout>
                </Route>
              ))}
            </Switch>
          )}
        />
      </LoginUserProvider>
      {/* 遷移画面に該当するパスが存在しない場合は 404 ページへ遷移 */}
      <Route path="*">
        <Page404 />
      </Route>
    </Switch>
  )
});