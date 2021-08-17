// ユーザー情報取得用カスタムフック
import { useCallback, useState } from "react";
import axios from "axios";

import { User } from "../types/api/user";
import { useMessage } from "./useMessage";

export const useAllUsers = () => {
  // カスタムフック
  // メッセージダイアログ表示のカスタムフック（ユーザ情報取得結果の表示）
  const { showMessage } = useMessage();

  // State
  // ユーザー情報取得の状態
  const [loading, setLoading] = useState(false);
  // ユーザー情報
  const [users, setUsers] = useState<Array<User>>([]);

  const getUsers = useCallback(
    () => {
      setLoading(true);
      axios
        // サンプルとして JSONPlaceholder を利用する
        // 正常にデータ取得できた場合の処理は then で記載記載する
        .get<Array<User>>("https://jsonplaceholder.typicode.com/users")
        .then((res) => { setUsers(res.data) })
        .catch(() => {
          showMessage({ title: "ユーザーの取得に失敗しました", status: "error" });
        })
        .finally(() => {
          setLoading(false)
        });
    },
    // eslint-disable-next-line
    [],
  );
  // ユーザ取得用関数、ユーザ取得の状態、ユーザー情報を戻す
  return { getUsers, loading, users };
};
