// ログインページのコンポーネント
import { memo, ChangeEvent, useState, VFC } from "react";
import { Box, Divider, Flex, Heading, Input, Stack } from "@chakra-ui/react";

import { PrimaryButton } from "../atoms/button/PrimaryButton";
import { useAuth } from "../../hooks/useAuth";

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const Login: VFC = memo(() => {
  // State
  // ユーザーID
  const [userId, setUserId] = useState('');

  // カスタムフック
  // 認証結果と認証の状態を示す変数を　useAuth にて定義
  const { login, loading } = useAuth();

  // イベント
  // ユーザーID State のセット
  // 入力時のイベントは e: ChangeEvent<HTMLInputElement で取得し、
  // e.target.valueで設定する
  const onChangeUserId = (e: ChangeEvent<HTMLInputElement>) => setUserId(e.target.value);
  // ログインボタン押下時の処理
  const onClickLogin = () => login(userId);

  return (
    <Flex align="center" justify="center" height="100vh">
      <Box bg="white" w="sm" p={4} borderRadius="md" shadow="md">
        <Heading as="h1" size="lg" textAlign="center">ユーザー管理アプリ</Heading>
        <Divider my={4} />
        <Stack spacing={6} py={4} px={10}>
          <Input placeholder="ユーザーID" value={userId} onChange={onChangeUserId} />
          <PrimaryButton
            disabled={userId === ""}
            loading={loading}
            onClick={onClickLogin}
          >
            ログイン
          </PrimaryButton>
        </Stack>
      </Box>
    </Flex>
  );
});