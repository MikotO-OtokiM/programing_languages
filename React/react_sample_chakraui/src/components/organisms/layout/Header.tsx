// ヘッダーのコンポーネント
import { memo, useCallback, VFC } from "react";
import { Box, Flex, Heading, Link, useDisclosure } from "@chakra-ui/react";
import { useHistory } from "react-router-dom";

import { MenuIconButton } from "../../atoms/button/MenuIconButton";
import { MenuDrower } from "../../molecules/MenuDrower";
import { useLoginUser } from "../../../hooks/useLoginUser";

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const Header: VFC = memo(() => {
  // カスタムフック
  // ログインユーザ情報を Context にセットするカスタムフック
  const { setLonginUser } = useLoginUser();

  // メニューアイコンの閉じ・開きは useDisclosure で管理できる
  const { isOpen, onOpen, onClose } = useDisclosure()

  // 画面遷移は useHistory を利用する
  const history = useHistory();
  // history.push で遷移先を指定
  // 不要なレンダリングを避けるため useCallback で囲う
  const onClickHome = useCallback(() => { history.push("/home") }, [history],);
  const onClickUserManagement = useCallback(() => { history.push("/home/user_management") }, [history],);
  const onClickSetting = useCallback(() => { history.push("/home/setting") }, [history],);
  const onClickLogout = useCallback(() => {
    // ログインユーザー情報をクリアしログイン画面へ遷移
    setLonginUser(null);
    history.push("/")
  }, [history, setLonginUser]);

  return (
    <>
      {/* 要素を横並びにするため Flex で囲う */}
      <Flex
        as="nav"
        bg="teal.500"
        color="gray.50"
        align="center"
        justify="space-between"
        padding={{ base: 3, md: 5 }}
      >
        <Flex
          align="center"
          as="a"
          mr={8}
          _hover={{ cursor: "pointer" }}
          onClick={onClickHome}
        >
          <Heading as="h1" fontSize={{ base: "md", md: "lg" }}>
            ユーザ管理アプリ
          </Heading>
        </Flex>
        <Flex
          align="center"
          fontSize="sm"
          flexGrow={2}
          display={{ base: "none", md: "flex" }}
        >
          <Box pr={4}>
            <Link onClick={onClickUserManagement}>ユーザ一覧</Link>
          </Box>
          <Box pr={4}>
            <Link onClick={onClickSetting}>設定</Link>
          </Box>
          <Link onClick={onClickLogout}>ログアウト</Link>
        </Flex>
        <MenuIconButton onOpen={onOpen} />
      </Flex>
      <MenuDrower
        onClose={onClose}
        isOpen={isOpen}
        onClickHome={onClickHome}
        onClickUserManagement={onClickUserManagement}
        onClickSetting={onClickSetting}
        onClickLogout={onClickLogout}
      />
    </>
  );
});