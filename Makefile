# Variables
I_TESTER = imgtest
TESTER = stock

V_TEST = $(PWD)/test:/home/dev/test

all: dock
# Ejecuta contenedor creado
exec:
	@docker exec -it $(TESTER) bash

# Genera nuevo contenedor docker
dock: image
	@docker rm -fv $(TESTER) && docker run --name $(TESTER) -v $(V_TEST) -id $(I_TESTER)

# Genera imagen docker
image:
	@docker build -t $(I_TESTER) .

# Elimina contenedor 
clean:
	@docker rm -fv $(TESTER)

# Elimina imagen
fclean: clean
	@docker rmi $(I_TESTER)

# Elimina y crea una nueva imagen y un nuevo contenedor
re: fclean all 