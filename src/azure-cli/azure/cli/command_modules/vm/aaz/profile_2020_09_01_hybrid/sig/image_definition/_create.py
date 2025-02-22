# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Create(AAZCommand):
    """Create a gallery image definition.
    """

    _aaz_info = {
        "version": "2021-10-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries/{}/images/{}", "2021-10-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gallery_image_name = AAZStrArg(
            options=["-n", "--name", "--gallery-image-name"],
            help="The name of the gallery image definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.",
            required=True,
        )
        _args_schema.gallery_name = AAZStrArg(
            options=["-r", "--gallery-name"],
            help="The name of the Shared Image Gallery in which the Image Definition resides.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "GalleryImage"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="GalleryImage",
            help="Resource location",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="GalleryImage",
            help="Resource tags",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.architecture = AAZStrArg(
            options=["--architecture"],
            arg_group="Properties",
            help="The architecture of the image. Applicable to OS disks only.",
            enum={"Arm64": "Arm64", "x64": "x64"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="The description of this gallery image definition resource. This property is updatable.",
        )
        _args_schema.disallowed = AAZObjectArg(
            options=["--disallowed"],
            arg_group="Properties",
            help="Describes the disallowed disk types.",
        )
        _args_schema.end_of_life_date = AAZDateTimeArg(
            options=["--end-of-life-date"],
            arg_group="Properties",
            help="The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.",
        )
        _args_schema.eula = AAZStrArg(
            options=["--eula"],
            arg_group="Properties",
            help="The Eula agreement for the gallery image definition.",
        )
        _args_schema.features = AAZListArg(
            options=["--features"],
            arg_group="Properties",
            help="A list of gallery image features.",
        )
        _args_schema.hyper_v_generation = AAZStrArg(
            options=["--hyper-v-generation"],
            arg_group="Properties",
            help="The hypervisor generation of the Virtual Machine. Applicable to OS disks only.",
            enum={"V1": "V1", "V2": "V2"},
        )
        _args_schema.identifier = AAZObjectArg(
            options=["--identifier"],
            arg_group="Properties",
            help="This is the gallery image definition identifier.",
        )
        _args_schema.os_state = AAZStrArg(
            options=["--os-state"],
            arg_group="Properties",
            help="This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.",
            enum={"Generalized": "Generalized", "Specialized": "Specialized"},
        )
        _args_schema.os_type = AAZStrArg(
            options=["--os-type"],
            arg_group="Properties",
            help="This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**",
            enum={"Linux": "Linux", "Windows": "Windows"},
        )
        _args_schema.privacy_statement_uri = AAZStrArg(
            options=["--privacy-statement-uri"],
            arg_group="Properties",
            help="The privacy statement uri.",
        )
        _args_schema.purchase_plan = AAZObjectArg(
            options=["--purchase-plan"],
            arg_group="Properties",
            help="Describes the gallery image definition purchase plan. This is used by marketplace images.",
        )
        _args_schema.recommended = AAZObjectArg(
            options=["--recommended"],
            arg_group="Properties",
            help="The properties describe the recommended machine configuration for this Image Definition. These properties are updatable.",
        )
        _args_schema.release_note_uri = AAZStrArg(
            options=["--release-note-uri"],
            arg_group="Properties",
            help="The release note uri.",
        )

        disallowed = cls._args_schema.disallowed
        disallowed.disk_types = AAZListArg(
            options=["disk-types"],
            help="A list of disk types.",
        )

        disk_types = cls._args_schema.disallowed.disk_types
        disk_types.Element = AAZStrArg()

        features = cls._args_schema.features
        features.Element = AAZObjectArg()

        _element = cls._args_schema.features.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the gallery image feature.",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value of the gallery image feature.",
        )

        identifier = cls._args_schema.identifier
        identifier.offer = AAZStrArg(
            options=["offer"],
            help="The name of the gallery image definition offer.",
            required=True,
        )
        identifier.publisher = AAZStrArg(
            options=["publisher"],
            help="The name of the gallery image definition publisher.",
            required=True,
        )
        identifier.sku = AAZStrArg(
            options=["sku"],
            help="The name of the gallery image definition SKU.",
            required=True,
        )

        purchase_plan = cls._args_schema.purchase_plan
        purchase_plan.name = AAZStrArg(
            options=["name"],
            help="The plan ID.",
        )
        purchase_plan.product = AAZStrArg(
            options=["product"],
            help="The product ID.",
        )
        purchase_plan.publisher = AAZStrArg(
            options=["publisher"],
            help="The publisher ID.",
        )

        recommended = cls._args_schema.recommended
        recommended.memory = AAZObjectArg(
            options=["memory"],
        )
        cls._build_args_resource_range_create(recommended.memory)
        recommended.v_cp_us = AAZObjectArg(
            options=["v-cp-us"],
            help="Describes the resource range.",
        )
        cls._build_args_resource_range_create(recommended.v_cp_us)
        return cls._args_schema

    _args_resource_range_create = None

    @classmethod
    def _build_args_resource_range_create(cls, _schema):
        if cls._args_resource_range_create is not None:
            _schema.max = cls._args_resource_range_create.max
            _schema.min = cls._args_resource_range_create.min
            return

        cls._args_resource_range_create = AAZObjectArg()

        resource_range_create = cls._args_resource_range_create
        resource_range_create.max = AAZIntArg(
            options=["max"],
            help="The maximum number of the resource.",
        )
        resource_range_create.min = AAZIntArg(
            options=["min"],
            help="The minimum number of the resource.",
        )

        _schema.max = cls._args_resource_range_create.max
        _schema.min = cls._args_resource_range_create.min

    def _execute_operations(self):
        self.pre_operations()
        yield self.GalleryImagesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class GalleryImagesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{galleryImageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "galleryImageName", self.ctx.args.gallery_image_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "galleryName", self.ctx.args.gallery_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-10-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("architecture", AAZStrType, ".architecture")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("disallowed", AAZObjectType, ".disallowed")
                properties.set_prop("endOfLifeDate", AAZStrType, ".end_of_life_date")
                properties.set_prop("eula", AAZStrType, ".eula")
                properties.set_prop("features", AAZListType, ".features")
                properties.set_prop("hyperVGeneration", AAZStrType, ".hyper_v_generation")
                properties.set_prop("identifier", AAZObjectType, ".identifier", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("osState", AAZStrType, ".os_state", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("osType", AAZStrType, ".os_type", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("privacyStatementUri", AAZStrType, ".privacy_statement_uri")
                properties.set_prop("purchasePlan", AAZObjectType, ".purchase_plan")
                properties.set_prop("recommended", AAZObjectType, ".recommended")
                properties.set_prop("releaseNoteUri", AAZStrType, ".release_note_uri")

            disallowed = _builder.get(".properties.disallowed")
            if disallowed is not None:
                disallowed.set_prop("diskTypes", AAZListType, ".disk_types")

            disk_types = _builder.get(".properties.disallowed.diskTypes")
            if disk_types is not None:
                disk_types.set_elements(AAZStrType, ".")

            features = _builder.get(".properties.features")
            if features is not None:
                features.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.features[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

            identifier = _builder.get(".properties.identifier")
            if identifier is not None:
                identifier.set_prop("offer", AAZStrType, ".offer", typ_kwargs={"flags": {"required": True}})
                identifier.set_prop("publisher", AAZStrType, ".publisher", typ_kwargs={"flags": {"required": True}})
                identifier.set_prop("sku", AAZStrType, ".sku", typ_kwargs={"flags": {"required": True}})

            purchase_plan = _builder.get(".properties.purchasePlan")
            if purchase_plan is not None:
                purchase_plan.set_prop("name", AAZStrType, ".name")
                purchase_plan.set_prop("product", AAZStrType, ".product")
                purchase_plan.set_prop("publisher", AAZStrType, ".publisher")

            recommended = _builder.get(".properties.recommended")
            if recommended is not None:
                _CreateHelper._build_schema_resource_range_create(recommended.set_prop("memory", AAZObjectType, ".memory"))
                _CreateHelper._build_schema_resource_range_create(recommended.set_prop("vCPUs", AAZObjectType, ".v_cp_us"))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _CreateHelper._build_schema_gallery_image_read(cls._schema_on_200_201)

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_resource_range_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("max", AAZIntType, ".max")
        _builder.set_prop("min", AAZIntType, ".min")

    _schema_gallery_image_read = None

    @classmethod
    def _build_schema_gallery_image_read(cls, _schema):
        if cls._schema_gallery_image_read is not None:
            _schema.id = cls._schema_gallery_image_read.id
            _schema.location = cls._schema_gallery_image_read.location
            _schema.name = cls._schema_gallery_image_read.name
            _schema.properties = cls._schema_gallery_image_read.properties
            _schema.tags = cls._schema_gallery_image_read.tags
            _schema.type = cls._schema_gallery_image_read.type
            return

        cls._schema_gallery_image_read = _schema_gallery_image_read = AAZObjectType()

        gallery_image_read = _schema_gallery_image_read
        gallery_image_read.id = AAZStrType(
            flags={"read_only": True},
        )
        gallery_image_read.location = AAZStrType(
            flags={"required": True},
        )
        gallery_image_read.name = AAZStrType(
            flags={"read_only": True},
        )
        gallery_image_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        gallery_image_read.tags = AAZDictType()
        gallery_image_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_gallery_image_read.properties
        properties.architecture = AAZStrType()
        properties.description = AAZStrType()
        properties.disallowed = AAZObjectType()
        properties.end_of_life_date = AAZStrType(
            serialized_name="endOfLifeDate",
        )
        properties.eula = AAZStrType()
        properties.features = AAZListType()
        properties.hyper_v_generation = AAZStrType(
            serialized_name="hyperVGeneration",
        )
        properties.identifier = AAZObjectType(
            flags={"required": True},
        )
        properties.os_state = AAZStrType(
            serialized_name="osState",
            flags={"required": True},
        )
        properties.os_type = AAZStrType(
            serialized_name="osType",
            flags={"required": True},
        )
        properties.privacy_statement_uri = AAZStrType(
            serialized_name="privacyStatementUri",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.purchase_plan = AAZObjectType(
            serialized_name="purchasePlan",
        )
        properties.recommended = AAZObjectType()
        properties.release_note_uri = AAZStrType(
            serialized_name="releaseNoteUri",
        )

        disallowed = _schema_gallery_image_read.properties.disallowed
        disallowed.disk_types = AAZListType(
            serialized_name="diskTypes",
        )

        disk_types = _schema_gallery_image_read.properties.disallowed.disk_types
        disk_types.Element = AAZStrType()

        features = _schema_gallery_image_read.properties.features
        features.Element = AAZObjectType()

        _element = _schema_gallery_image_read.properties.features.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        identifier = _schema_gallery_image_read.properties.identifier
        identifier.offer = AAZStrType(
            flags={"required": True},
        )
        identifier.publisher = AAZStrType(
            flags={"required": True},
        )
        identifier.sku = AAZStrType(
            flags={"required": True},
        )

        purchase_plan = _schema_gallery_image_read.properties.purchase_plan
        purchase_plan.name = AAZStrType()
        purchase_plan.product = AAZStrType()
        purchase_plan.publisher = AAZStrType()

        recommended = _schema_gallery_image_read.properties.recommended
        recommended.memory = AAZObjectType()
        cls._build_schema_resource_range_read(recommended.memory)
        recommended.v_cp_us = AAZObjectType(
            serialized_name="vCPUs",
        )
        cls._build_schema_resource_range_read(recommended.v_cp_us)

        tags = _schema_gallery_image_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_gallery_image_read.id
        _schema.location = cls._schema_gallery_image_read.location
        _schema.name = cls._schema_gallery_image_read.name
        _schema.properties = cls._schema_gallery_image_read.properties
        _schema.tags = cls._schema_gallery_image_read.tags
        _schema.type = cls._schema_gallery_image_read.type

    _schema_resource_range_read = None

    @classmethod
    def _build_schema_resource_range_read(cls, _schema):
        if cls._schema_resource_range_read is not None:
            _schema.max = cls._schema_resource_range_read.max
            _schema.min = cls._schema_resource_range_read.min
            return

        cls._schema_resource_range_read = _schema_resource_range_read = AAZObjectType()

        resource_range_read = _schema_resource_range_read
        resource_range_read.max = AAZIntType()
        resource_range_read.min = AAZIntType()

        _schema.max = cls._schema_resource_range_read.max
        _schema.min = cls._schema_resource_range_read.min


__all__ = ["Create"]
