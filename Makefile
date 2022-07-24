I_TESTER = imgtest
TESTER = stock

V_SRCCODE = $(PWD)/code:/home/dev/code
V_TEST = $(PWD)/infection:/home/dev/infection

all: dock

image:
	@docker build -t $(I_TESTER) .

dock: image
	@docker rm -fv $(TESTER) && docker run --name $(TESTER) -v $(V_SRCCODE) -v $(V_TEST) -id $(I_TESTER)

exec:
	@docker exec -it $(TESTER) bash

clean:
	@docker rm -fv $(TESTER)

fclean: clean
	@docker rmi $(I_TESTER)

re: fclean all 
