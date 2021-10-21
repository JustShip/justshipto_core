import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from justship.apps.core.models import Tag
from justship.apps.products.models import Product
from .types import ProductType


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String()
        description = graphene.String(required=False)
        link = graphene.String(required=False)
        state = graphene.String()
        tags = graphene.List(graphene.String, required=False)

    @staticmethod
    @login_required
    def mutate(root, info, name, state, description=None, link=None, tags=None):
        user = info.context.user

        try:
            new_product = Product(name=name,
                                  state=state,
                                  description=description,
                                  link=link,
                                  owner=user
                                  )
            new_product.save()
            if tags:
                tags_list = Tag.objects.filter(name__in=tags)
                new_product.tags.add(*tags_list)
            new_product.save()
            return CreateProduct(product=new_product)

        except:
            return GraphQLError("Object with same name already exists")


class ProductMutations:
    create_product = CreateProduct.Field()
