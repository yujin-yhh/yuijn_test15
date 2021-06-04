import allure


def handle_blacklist(func):
    def wrapper(*args, **kwargs):
        from snowball.pages.basepage import BasePage
        # instance是BasePage的一个实例
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
            # 捕获黑名单中的元素
        except Exception as e:
            # 进入异常程序则截图并上传到allure报告中
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 如果超过最大错误次数，抛出异常
            if instance.error_num > instance.max_num:
                raise e
            # 只要进入捕获异常流程，则错误次数+1
            instance.error_num += 1
            # 从黑名单中遍历元素，依次查找
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单后再次查找原来的元素
                    return wrapper(*args, **kwargs)
            # 如果元素未在黑名单中，抛出异常
            raise e

    return wrapper
